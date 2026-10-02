import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

def build_model():
    # Base model using MobileNetV2
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    base_model.trainable = False

    # Custom classification head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(128, activation='relu')(x)
    predictions = Dense(3, activation='softmax')(x)  # Organic, Recyclable, Hazardous

    model = Model(inputs=base_model.input, outputs=predictions)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

if __name__ == "__main__":
    print("Building EcoSort AI Model...")
    model = build_model()
    model.summary()
    # Save placeholder weights structure
    model.save("ecosort_model.h5")
    print("Model architecture built and saved successfully as ecosort_model.h5!")
  
