#password = input("Enter Passowrd: ")

def check_password_strength(password):
  """
  Checks the strength of a password and provides feedback.

  Args:
    password: The password to check.

  Returns:
    A string indicating the password strength ("Weak", "Medium", or "Strong").
  """
  strength = "Weak"
  if len(password) >= 6:
    strength = "Medium"
    if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
      strength = "Strong"
  return strength

def get_password_feedback(strength):
  """
  Provides feedback based on the password strength.

  Args:
    strength: The password strength ("Weak", "Medium", or "Strong").

  Returns:
    A string with the feedback message.
  """
  if strength == "Weak":
    return "Your password is too weak. Please try again with a longer password."
  elif strength == "Medium":
    return "Your password is medium strength. Consider adding special characters like !@#$%^&*() to make it stronger."
  else:
    return "Congratulations! You have a strong password."

while True:
  password = input("Enter a password: ")
  strength = check_password_strength(password)
  feedback = get_password_feedback(strength)
  print(feedback)
  if strength == "Strong":
    break