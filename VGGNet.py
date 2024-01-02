import tensorflow as tf
from keras import layers, models

def vgg_block(x, num_filters, num_conv_layers):
    for _ in range(num_conv_layers):
        x = layers.Conv2D(num_filters, (3, 3), padding='same', activation='relu')(x)
    x = layers.MaxPooling2D((2, 2), strides=(2, 2))(x)
    return x

def vggnet(input_shape, num_classes):
    input_layer = layers.Input(shape=input_shape)

    # Block 1
    x = vgg_block(input_layer, 64, 2)

    # Block 2
    x = vgg_block(x, 128, 2)

    # Block 3
    x = vgg_block(x, 256, 3)

    # Block 4
    x = vgg_block(x, 512, 3)

    # Block 5
    x = vgg_block(x, 512, 3)

    # Flatten and fully connected layers
    x = layers.Flatten()(x)
    x = layers.Dense(4096, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(4096, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(num_classes, activation='softmax')(x)

    model = models.Model(inputs=input_layer, outputs=x)

    return model

# Example usage:
input_shape = (224, 224, 3)  # Example input shape for RGB images
num_classes = 1000  # Example number of classes for ImageNet

model = vggnet(input_shape, num_classes)
model.summary()