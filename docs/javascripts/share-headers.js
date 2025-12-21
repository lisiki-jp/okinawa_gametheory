document$.subscribe(function() {
  // 1. Target H2 and H3 only
  const headers = document.querySelectorAll("article h2, article h3");

  headers.forEach(header => {
    if (header.querySelector(".share-button")) return;

    // 2. Create the indigo button
    const shareBtn = document.createElement("button");
    shareBtn.classList.add("share-button"); 
    shareBtn.setAttribute("title", "Share this section");
    
    // Using a clear "Share" icon (SVG)
    shareBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81a3 3 0 0 0 3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9a3 3 0 0 0-3 3 3 3 0 0 0 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.15c-.05.21-.08.43-.08.66 0 1.61 1.31 2.91 2.92 2.91s2.92-1.3 2.92-2.91a2.92 2.92 0 0 0-2.92-2.91"/></svg>';

    shareBtn.onclick = (e) => {
      e.stopPropagation();
      
      // Extract title and remove the ¶ icon if present
      const cleanTitle = header.innerText.replace("¶", "").trim();
      const shareUrl = window.location.origin + window.location.pathname + "#" + header.id;

      if (navigator.share) {
        navigator.share({
          title: cleanTitle,
          text: cleanTitle, 
          url: shareUrl
        }).catch(() => {});
      } else {
        // Fallback for desktop browsers without Share API
        navigator.clipboard.writeText(`${cleanTitle} - ${shareUrl}`);
        alert("Link copied!");
      }
    };

    header.appendChild(shareBtn);
  });
});
