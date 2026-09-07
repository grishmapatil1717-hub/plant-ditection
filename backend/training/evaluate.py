import argparse
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model_path: str, val_generator):
    import tensorflow as tf
    from sklearn.metrics import classification_report, confusion_matrix

    model = tf.keras.models.load_model(model_path)
    val_generator.reset()
    predictions = model.predict(val_generator)
    y_pred = np.argmax(predictions, axis=1)
    y_true = val_generator.classes
    labels = list(val_generator.class_indices.keys())

    print("=== Classification Report ===")
    print(classification_report(y_true, y_pred, target_names=labels))

    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Greens", xticklabels=labels, yticklabels=labels)
    plt.title(f"Confusion Matrix: {Path(model_path).stem}")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.tight_layout()
    plt.savefig(f"{Path(model_path).stem}_confusion_matrix.png", dpi=300)
    print(f"Confusion matrix saved as {Path(model_path).stem}_confusion_matrix.png")
