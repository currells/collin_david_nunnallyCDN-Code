// Counter for participants
let participantCount = 1;


//Adding a participant on clicking a button
document.addEventListener("DOMContentLoaded", function () {
    const addButton = document.getElementById("addParticipant"); // Loads DOM before running

    addButton.addEventListener("click", function () {
        participantCount++;
        const newParticipant = participantTemplate(participantCount);
        addButton.insertAdjacentHTML("beforebegin", newParticipant);
    });
});

// Template for new participant
function participantTemplate(count) {
    return `
    <section class="participant${count}">
        <label for="name${count}">Participant ${count} Name:</label>
        <input type="text" id="name${count}" name="name${count}">
        
        <label for="fee${count}">Fee:</label>
        <input type="number" id="fee${count}" name="fee${count}" value="0">
    </section>`;
}

// Form submission
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registrationForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        let totalFee = totalFees();
        let adultName = document.getElementById("adultName").value;
        let participantCount = document.querySelectorAll("[id^=name]").length;

        document.getElementById("formContainer").style.display = "none";
        document.getElementById("summary").innerHTML = successTemplate(adultName, participantCount, totalFee);
        document.getElementById("summary").classList.remove("hide");
    });
});


//Calculates fees and adds them together
function totalFees() {
    let feeElements = [...document.querySelectorAll("[id^=fee]")];
    return feeElements.reduce((sum, fee) => sum + Number(fee.value), 0);
}


//Shows success message once form is submitted
function successTemplate(name, count, fee) {
    return `<p>Thank you, ${name}, for registering. You have registered ${count} participants and owe $${fee} in Fees.</p>`;
}
