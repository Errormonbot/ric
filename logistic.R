install.packages('ggplot2')
library(ggplot2)

hours <- c(1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6)  # Independent variable (hours of study)
pass_fail <- c(0, 0, 0, 0, 0, 1, 1, 1, 1, 1)  # Dependent variable (pass=1, fail=0)

data <- data.frame(hours, pass_fail)

logit_model <- glm(pass_fail ~ hours, data = data, family = "binomial")

summary(logit_model)

# Predicting the probability for a range of values
# Create a sequence of hours from 0 to 7 to predict probabilities
new_data <- data.frame(hours = seq(0, 7, by = 0.1))
new_data$predicted_prob <- predict(logit_model, newdata = new_data, type = "response")

#Plot the logistic regression curve with data points
ggplot(data, aes(x = hours, y = pass_fail)) +
  geom_point(color = "blue", size = 3) +  # Plot the actual data points
  geom_line(data = new_data, aes(x = hours, y = predicted_prob), color = "red") +  # Plot the logistic curve
  labs(title = "Logistic Regression: Hours of Study vs Probability of Passing",
       x = "Hours of Study",
       y = "Probability of Passing") +
  theme_minimal() +
  scale_y_continuous(breaks = seq(0, 1, 0.1))  # Customize y-axis to show probabilities
