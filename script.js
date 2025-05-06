window.onload = () => {
    fetch('/songs')
      .then(response => response.json())
      .then(songs => {
        const list = document.getElementById('songList');
        const player = document.getElementById('audioPlayer');
        songs.forEach(song => {
          const li = document.createElement('li');
          li.textContent = song;
          li.onclick = () => {
            player.src = `/songs/${encodeURIComponent(song)}`;
            player.play();
          };
          list.appendChild(li);
        });
      });
  };
  