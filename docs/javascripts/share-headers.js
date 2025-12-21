// This works with Material for MkDocs "Instant Loading"
document$.subscribe(function() {
  // 1. Select H1, H2, and H3
  const headers = document.querySelectorAll("article h1, article h2, article h3");

  headers.forEach(header => {
    // Prevent duplicate buttons if the script runs twice
    if (header.querySelector(".share-button")) return;

    // 2. Create the button using Material's icon class
    const shareBtn = document.createElement("button");
    shareBtn.classList.add("share-button", "md-icon"); 
    shareBtn.setAttribute("title", "Share this section");
    
    // Using a standard Material "share" SVG icon
    shareBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81a3 3 0 0 0 3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9a3 3 0 0 0-3 3 3 3 0 0 0 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.15c-.05.21-.08.43-.08.66 0 1.61 1.31 2.91 2.92 2.91s2.92-1.3 2.92-2.91a2.92 2.92 0 0 0-2.92-2.91"/></svg>';

    shareBtn.onclick = (e) => {
      e.preventDefault();
      
      // 3. Generate Title (Site Name + Page Title + Section)
      const siteName = document.querySelector(".md-header__topic").innerText;
      const sectionTitle = header.innerText.trim();
      const fullTitle = `${siteName} - ${sectionTitle}`;
      const shareUrl = window.location.origin + window.location.pathname + "#" + header.id;

      if (navigator.share) {
        navigator.share({
          title: fullTitle,
          text: `Check this out: ${sectionTitle}`,
          url: shareUrl
        });
      } else {
        navigator.clipboard.writeText(shareUrl);
        // Optional: show a small Material toast here
      }
    };

    header.appendChild(shareBtn);
  });
});
