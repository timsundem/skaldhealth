document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");
  const confirmPasswordInput = document.getElementById("confirmPassword");
  const loginButton = document.getElementById("loginButton");
  const createAccountButton = document.getElementById("createAccountButton");
  const toggleForm = document.getElementById("toggleForm");
  const errorMessage = document.getElementById("errorMessage");
  const roleSelect = document.getElementById("role");

  let isCreatingAccount = false;

  // Toggle between Login and Create Account modes
  toggleForm.addEventListener("click", () => {
    isCreatingAccount = !isCreatingAccount;

    if (isCreatingAccount) {
      confirmPasswordInput.style.display = "block";
      roleSelect.style.display = "block";
      loginButton.style.display = "none";
      createAccountButton.style.display = "block";
      toggleForm.innerHTML = 'Already have an account? <span>Log in.</span>';
    } else {
      confirmPasswordInput.style.display = "none";
      roleSelect.style.display = "none";
      loginButton.style.display = "block";
      createAccountButton.style.display = "none";
      toggleForm.innerHTML = 'New here? <span>Create an account.</span>';
    }
  });

  // Handle Login Form Submission
  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    errorMessage.textContent = "";

    const email = emailInput.value;
    const password = passwordInput.value;

    if (isCreatingAccount) {
      const confirmPassword = confirmPasswordInput.value;
      const role = roleSelect.value;

      if (password !== confirmPassword) {
        errorMessage.textContent = "Passwords do not match.";
        return;
      }

      // Create Account API call
      try {
        const response = await fetch("http://127.0.0.1:5000/users", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email, password, role }), // Send selected role
        });

        if (response.ok) {
          const data = await response.json();
          console.log("Account created successfully:", data);
          errorMessage.textContent = "Account created successfully. Please log in.";
          toggleForm.click(); // Switch back to login mode
        } else {
          const errorData = await response.json();
          errorMessage.textContent = errorData.message || "Account creation failed.";
        }
      } catch (error) {
        console.error("Network error:", error);
        errorMessage.textContent = "Network error. Please try again.";
      }
    } else {
      // Login API call
      try {
        const response = await fetch("http://127.0.0.1:5000/auth/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email, password }),
        });

        if (response.ok) {
          const data = await response.json();
          console.log("Login successful:", data);

          // Save token to localStorage
          localStorage.setItem("token", data.token);

          // Redirect to home page
          window.location.href = "/home.html";
        } else {
          const errorData = await response.json();
          errorMessage.textContent = errorData.message || "Login failed.";
        }
      } catch (error) {
        console.error("Network error:", error);
        errorMessage.textContent = "Network error. Please try again.";
      }
    }
  });
});
