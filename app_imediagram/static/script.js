function openLightbox() {
    var lightbox = document.getElementById("lightbox");
    lightbox.style.display = "block";
}

function closeLightbox() {
    var lightbox = document.getElementById("lightbox");
    lightbox.style.display = "none";
}

// <div id="lightbox" class="lightbox">
//     <span class="close" onclick="closeLightbox()">&times;</span>
//     <img class="lightbox-content" src="imagem.jpg" alt="Imagem em tela cheia">
// </div>