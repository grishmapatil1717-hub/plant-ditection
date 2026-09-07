import os
from pathlib import Path
from typing import Tuple

def get_data_generators(
    data_dir: str,
    target_size: Tuple[int, int] = (224, 224),
    batch_size: int = 32,
    validation_split: float = 0.2
):
    """
    Creates training and validation image data generators with augmentation.
    """
    try:
        from tensorflow.keras.preprocessing.image import ImageDataGenerator
    except ImportError:
        raise ImportError("TensorFlow is required for dataset loading. Run: pip install tensorflow")

    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        rotation_range=25,
        width_shift_range=0.15,
        height_shift_range=0.15,
        shear_range=0.15,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode="nearest",
        validation_split=validation_split
    )

    val_datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        validation_split=validation_split
    )

    train_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode="categorical",
        subset="training",
        shuffle=True
    )

    val_generator = val_datagen.flow_from_directory(
        data_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode="categorical",
        subset="validation",
        shuffle=False
    )

    return train_generator, val_generator
