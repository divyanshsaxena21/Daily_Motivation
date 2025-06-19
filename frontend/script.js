async function generateMotivation() {
  const mood = document.getElementById("mood").value;
  const resultDiv = document.getElementById("result");

  if (!mood) {
    alert("Please select a mood.");
    return;
  }

  resultDiv.textContent = "Generating...";

  try {
    const response = await fetch("http://127.0.0.1:5000/generate", {
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
