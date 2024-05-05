from zenml import pipeline, step

@step
def load_data():
    print("loading_data...")
    return "I am data"

@step
def process_data():
    """Apply preprocessing steps to the data."""
    print("preprocessing...")
    return "I am processed data"

@step
def train_model():
    """Train a model on the processed data."""
    print("training model...")
    return "I am a trained model"

@pipeline
def my_pipeline():
    """My sample pipeline."""
    loaded_data = load_data()
    processed_data = process_data()
    trained_model = train_model()
    # Run the pipeline with ZenML
    return trained_model

if __name__ == "__main__":
    run = my_pipeline()
    print(f"The result of running the pipeline is:\n{run}")
    # You can now use the run object to see steps, outputs, etc.