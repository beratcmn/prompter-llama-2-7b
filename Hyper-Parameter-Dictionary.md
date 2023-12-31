# Hyper Parameter Dictionary

Info generated by ChatGPT (GPT-3.5-Turbo)

## Hyper-Parameters

- **Per device batch size:** This parameter determines the number of training examples processed in parallel on each device during training. In this case, the batch size is set to 1, meaning each training example is processed individually on each device. Smaller batch sizes can lead to more frequent weight updates but may result in slower training overall due to reduced parallelism.

- **Gradient accumulation steps:** This parameter determines the number of mini-batches that need to be processed before performing a weight update. In this case, the weight update is performed after accumulating gradients from 4 mini-batches. This technique allows for effectively simulating larger batch sizes without increasing memory requirements, as gradients are accumulated before the update step.

- **Epochs:** An epoch represents a complete pass through the entire training dataset. In this case, the training process involves going through the entire dataset 5 times.

- **Learning rate:** The learning rate determines the step size at which the optimizer adjusts the model's parameters during training. A learning rate of 2e-4 means that the model parameters are updated by this value times the gradient of the loss function. Adjusting the learning rate can affect the convergence speed and the quality of the final model.

- **Data type for weights:** This parameter determines the precision used to represent the model's weights. In this case, the weights are stored in float16 format, which is a 16-bit floating-point representation. Using a lower precision can reduce memory usage and training time but may also result in a slight loss of model accuracy compared to using higher precision, such as float32.

- **Save total limit:** This parameter specifies the maximum number of checkpoints or models that will be saved during the training process. In this case, a maximum of 3 models will be saved, potentially at different points in the training process.

- **Logging steps:** This parameter determines the frequency at which training metrics and logs are recorded. In this case, the model will log information after every training step.

- **Optimizer:** The optimizer determines the algorithm used to update the model's weights based on the computed gradients. In this case, the Paged AdamW 8-bit optimizer is used. It's a variant of the AdamW optimizer that supports 8-bit precision computation, which can help reduce memory usage during training.

- **LR scheduler:** The learning rate scheduler adjusts the learning rate over the course of training. In this case, the Cosine scheduler is used, which gradually reduces the learning rate following a cosine function. This schedule is often used to achieve a more gradual and smooth convergence.

- **Warmup Ratio:** The warmup ratio determines the proportion of the total number of training steps during which the learning rate gradually increases from zero to its initial value. In this case, the warmup ratio is set to 0.05, meaning that the learning rate will increase linearly for the first 5% of the total training steps before following the cosine schedule.

## Adjusting Hyper-Parameters

- **Per device batch size:**

  - <u>Increase:</u> A larger batch size can lead to faster training due to increased parallelism. However, it may also require more memory to store intermediate computations, and excessively large batch sizes can lead to convergence issues or degraded model performance.

  - <u>Decrease:</u> A smaller batch size can result in slower training as there is less parallelism. However, it can help improve model generalization and convergence, especially when dealing with limited memory or complex datasets.

- **Gradient accumulation steps:**

  - <u>Increase:</u> Increasing the number of gradient accumulation steps allows for more updates to the model's parameters before performing weight updates. This can help stabilize the training process, especially when using larger batch sizes or dealing with limited memory. However, it can also slow down training due to fewer weight updates per mini-batch.

  - <u>Decrease:</u> Decreasing the number of gradient accumulation steps can lead to more frequent weight updates, potentially accelerating the training process. However, it may also introduce more noise into the weight updates, which could affect model convergence and stability.

- **Epochs:**

  - <u>Increase:</u> Training for more epochs allows the model to see the training data multiple times, potentially leading to better convergence and improved performance. However, training for too many epochs can risk overfitting the model to the training data, resulting in poorer generalization on unseen data.

  - <u>Decrease:</u> Training for fewer epochs can reduce the overall training time. However, if the model has not converged or learned the underlying patterns in the data, reducing the number of epochs may result in suboptimal model performance.

- **Learning rate:**

  - <u>Increase:</u> Increasing the learning rate can speed up the training process as weight updates are more substantial. However, a high learning rate may also result in unstable training, causing the loss function to fluctuate or prevent the model from converging.

  - <u>Decrease:</u> Decreasing the learning rate can lead to more stable training and potentially better convergence. However, it may also slow down the training process and risk getting trapped in local optima.

- **Data type for weights:**

  - <u>Increase</u> precision (e.g., float32): Using higher precision for weights can potentially result in more accurate models as it allows for more fine-grained representation of numerical values. However, it comes at the cost of increased memory usage and longer training times.

  - <u>Decrease</u> precision (e.g., float16): Decreasing the precision can reduce memory usage and accelerate training. However, it may also introduce some loss of model accuracy due to the reduced precision's limited representation capability.

- **Save total limit:**

  - <u>Increase:</u> Increasing the save total limit allows for more checkpoints or models to be saved during training. This can provide more options for model selection or allow for better analysis of the training process. However, it also requires more storage space.

  - <u>Decrease:</u> Decreasing the save total limit reduces the number of checkpoints saved, which can save storage space. However, it may limit the ability to analyze the training process or choose the best-performing models.

- **Logging steps:**

  - <u>Increase:</u> Increasing the logging steps will result in more frequent recording of training metrics and logs. This can provide more detailed information about the training progress but also increases the amount of logged data.

  - <u>Decrease:</u> Decreasing the logging steps reduces the frequency of recorded training metrics and logs. This can save computational resources and reduce the amount of logged data. However, it may provide less detailed information about the training process.

- **Optimizer:**

  - Changing the optimizer can have various effects on the training process. Different optimizers have different update rules and convergence properties. It's worth experimenting with different optimizers to see which one works best for your specific task and model architecture.

- **LR scheduler:**

  - Changing the learning rate scheduler can impact how the learning rate changes during training. Different schedules can affect the convergence speed, stability, and ability to escape local optima. It's important to choose a scheduler that suits your training needs and the characteristics of your dataset.

- **Warmup Ratio:**

  - <u>Increase:</u> Increasing the warmup ratio means the learning rate gradually increases for a larger proportion of the training steps. This can be helpful when starting from very low learning rates or when dealing with complex or large models. It allows the model to explore the parameter space more thoroughly in the early stages of training.

  - <u>Decrease:</u> Decreasing the warmup ratio reduces the proportion of training steps during which the learning rate gradually increases. This may be useful when the model can quickly converge or when using a smaller model with a simpler dataset. It can help save training time by starting the learning rate at its initial value earlier in the training process.
