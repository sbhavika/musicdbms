// Array to store activity history
let activityHistory = [];

// Function to add a song to the list
function addSongToList(songTitle, artist) {
    const songList = document.getElementById("songList");
    const li = document.createElement("li");
    li.textContent = `${songTitle} - ${artist}`;
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.classList.add("delete-button");
    deleteButton.addEventListener("click", function() {
        deleteSong(li, songTitle, artist);
    });
    const updateButton = document.createElement("button");
    updateButton.textContent = "Update";
    updateButton.classList.add("update-button");
    updateButton.addEventListener("click", function() {
        updateSong(li, songTitle, artist);
    });
    li.appendChild(deleteButton);
    li.appendChild(updateButton);
    songList.appendChild(li);
    // Add activity to history
    const activity = `Added song: ${songTitle} - ${artist}`;
    activityHistory.push(activity);
    displayActivityHistory();
}

// Function to delete a song from the list
function deleteSong(li, songTitle, artist) {
    const songList = document.getElementById("songList");
    songList.removeChild(li);
    // Add activity to history
    const activity = `Deleted song: ${songTitle} - ${artist}`;
    activityHistory.push(activity);
    displayActivityHistory();
}

// Function to update a song in the list
function updateSong(li, songTitle, artist) {
    const newTitle = prompt("Enter new song title:", songTitle);
    const newArtist = prompt("Enter new artist name:", artist);
    if (newTitle !== null && newArtist !== null) {
        songTitle = newTitle.trim();
        artist = newArtist.trim();
        li.textContent = `${songTitle} - ${artist}`;
        // Add activity to history
        const activity = `Updated song: ${songTitle} - ${artist}`;
        activityHistory.push(activity);
        displayActivityHistory();
    }
}

// Function to display activity history
function displayActivityHistory() {
    const activityList = document.getElementById("activityList");
    activityList.innerHTML = "";
    activityHistory.forEach(activity => {
        const li = document.createElement("li");
        li.textContent = activity;
        activityList.appendChild(li);
    });
}

// Event listener for form submission (adding a song)
document.getElementById("musicForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const songTitle = document.getElementById("songTitle").value.trim();
    const artist = document.getElementById("artist").value.trim();
    if (songTitle && artist) {
        addSongToList(songTitle, artist);
        document.getElementById("songTitle").value = "";
        document.getElementById("artist").value = "";
    } else {
        alert("Please fill in both fields.");
    }
});
