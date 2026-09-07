import os
import argparse
from pathlib import Path

def build_model(architecture: str, num_classes: int, input_shape=(224, 224, 3)):
    import tensorflow as tf
    from tensorflow.keras import layers, models

    if architecture == "mobilenetv2":
        base_model = tf.keras.applications.MobileNetV2(
            input_shape=input_shape,
            include_top=False,
            weights="imagenet"
        )
        base_model.trainable = False
        x = layers.GlobalAveragePooling2D()(base_model.output)
        x = layers.BatchNormalization()(x)
        x = layers.Dense(256, activation="relu")(x)
        x = layers.Dropout(0.3)(x)
        outputs = layers.Dense(num_classes, activation="softmax")(x)
        model = models.Model(inputs=base_model.input, outputs=outputs)
    elif architecture == "resnet50":
        base_model = tf.keras.applications.ResNet50(
            input_shape=input_shape,
            include_top=False,
            weights="imagenet"
        )
        base_model.trainable = False
        x = layers.GlobalAveragePooling2D()(base_model.output)
        x = layers.Dense(512, activation="relu")(x)
        x = layers.Dropout(0.4)(x)
        outputs = layers.Dense(num_classes, activation="softmax")(x)
        model = models.Model(inputs=base_model.input, outputs=outputs)
    else:
        # Custom CNN
        model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation="relu", input_shape=input_shape),
            layers.MaxPooling2D(2, 2),
            layers.Conv2D(64, (3, 3), activation="relu"),
            layers.MaxPooling2D(2, 2),
            layers.Conv2D(128, (3, 3), activation="relu"),
            layers.MaxPooling2D(2, 2),
            layers.Conv2D(256, (3, 3), activation="relu"),
            layers.MaxPooling2D(2, 2),
            layers.Flatten(),
            layers.Dense(256, activation="relu"),
            layers.Dropout(0.4),
            layers.Dense(num_classes, activation="softmax")
        ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model

def main():
    parser = argparse.ArgumentParser(description="Train Deep Learning Crop Disease Classifier")
    parser.add_argument("--crop", type=str, required=True, choices=["potato", "tomato", "apple", "corn", "grape"])
    parser.add_argument("--data_dir", type=str, default="dataset")
    parser.add_argument("--arch", type=str, default="mobilenetv2", choices=["mobilenetv2", "resnet50", "cnn"])
    parser.add_argument("--epochs", type=int, default=25)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--output", type=str, default="models")
    args = parser.parse_args()

    import tensorflow as tf
    from backend.training.dataset_loader import get_data_generators

    print(f"=== Starting Training for {args.crop.upper()} [{args.arch}] ===")
    train_gen, val_gen = get_data_generators(args.data_dir, batch_size=args.batch_size)
    num_classes = train_gen.num_classes

    model = build_model(args.arch, num_classes)
    model.summary()

    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(factor=0.2, patience=3),
        tf.keras.callbacks.ModelCheckpoint(f"{args.output}/{args.crop}_model.keras", save_best_only=True)
    ]

    history = model.fit(
        train_gen,
        validation_data=val_gen,
        epochs=args.epochs,
        callbacks=callbacks
    )

    print(f"Training complete. Saved to {args.output}/{args.crop}_model.keras")

if __name__ == "__main__":
    main()
