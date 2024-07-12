import replicate
import os
import time
import torch

if torch.cuda.is_available():
    print("CUDA is available. Using GPU.")
else:
    print("CUDA is not available. Using CPU.")

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", None)

# dataset_path: A URL pointing to your zip or audio file
# one_same_description: A description for all audio data (default: none)
# auto_labeling: Creates label data like genre, mood, theme, instrumentation, key, bpm for each track. Using essentia-tensorflow for music information retrieval (default: true)
# drop_vocals: Drops vocal tracks from audio files in the dataset, by separating sources with Demucs (default: true)
# model_version: The model version to train, choices are “melody”, “small”, “medium” (default: “small”)
# lr: Learning rate (default: 1)
# epochs: Number of epochs to train for (default: 3)
# updates_per_epoch: Number of iterations for one epoch (default: 100). If set to None, iterations per epoch will be determined automatically based on batch size and dataset.
# batch_size: Batch size, must be a multiple of 8 (default: 16)

training = replicate.trainings.create(
    version="sakemin/musicgen-fine-tuner:8d02c56b9a3d69abd2f1d6cc1a65027de5bfef7f0d34bd23e0624ecabb65acac",
    input={
        "dataset_path": "https://replicate.delivery/pbxt/LFh5K7OroehspoHhx8kRBwAPFVnLpFEgxDKRsgLcpraxzzaC/data.zip",
        "auto_labeling": False,
        "drop_vocals": True,
        "model_version": "small",
    },
    destination="hugof-silva/musicgen-modao-de-buteco"
)

while training.status not in ["completed", "failed"]:
    training.reload()
    print(training.status)
    print("\n".join(training.logs.split("\n")[-10:]))
    time.sleep(30)

if training.status == "completed":
    print("Training completed successfully!")
elif training.status == "failed":
    print("Training failed. Check logs for details.")