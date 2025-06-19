async function generateMotivation() {
  const mood = document.getElementById("mood").value;
  const resultDiv = document.getElementById("result");

  if (!mood) {
    alert("Please select a mood.");
    return;
  }

  resultDiv.textContent = "Generating...";

  try {
    const response = await fetch("https://daily-motivation-tqds.onrender.com/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ mood })
    });

    const data = await response.json();
    resultDiv.textContent = data.result;
  } catch (error) {
    resultDiv.textContent = "Something went wrong. Try again!";
    console.error(error);
  }
}
