// Update the video player and display the result overlay
function updateVideoPlayer(videoUrl, result) {
  var videoPlayer = document.getElementById('videoPlayer');
  var resultOverlay = document.getElementById('resultOverlay');

  videoPlayer.src = videoUrl;
  videoPlayer.play();
  console.log(result)
  if (result.results === 'abnormal') {
    resultOverlay.innerHTML = '<h2>Abnormal Event Detected</h2>';
    resultOverlay.style.display = 'block';
  } else if (result.results === "normal") {
    resultOverlay.innerHTML = '<h2>No Abnormal Event Detected</h2>';
    resultOverlay.style.display = 'block';
  } else {
    resultOverlay.innerHTML = '<h2>No result available</h2>';
    resultOverlay.style.display = 'block';
  }
  console.log(resultOverlay);
  console.log(result[0].results);
  console.log(result[0]);


}
// Handle form submission
document.getElementById('uploadForm').addEventListener('submit', function(event) {
  event.preventDefault();
  var form = event.target;
  var videoFile = form.elements.video.files[0];
  var formData = new FormData();
  formData.append('video', videoFile);

  fetch(form.action, {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        alert(data.error);
      } else {
        var videoUrl = URL.createObjectURL(videoFile);
        updateVideoPlayer(videoUrl, data.result);
      }
    })
    .catch(error => {
      console.error(error);
      alert('An error occurred during video analysis.');
    });
});
