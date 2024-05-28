function makeChoice(choice) {
    fetch(`/play?choice=${choice}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('resultText').innerText = data.result;
            document.getElementById('userChoiceImg').src = `images/${choice}.png`;
            document.getElementById('userChoiceImg').alt = choice;
            document.getElementById('computerChoiceImg').src = `images/${data.computer_choice}.png`;
            document.getElementById('computerChoiceImg').alt = data.computer_choice;
        });
}
