document$.subscribe(function() {
  // 1. Target H1, H2, and H3
  const headers = document.querySelectorAll("article h1, article h2, article h3");

  headers.forEach(header => {
    if (header.querySelector(".share-button")) return;

    // 2. Create the Indigo Bullet Button
    const shareBtn = document.createElement("button");
    shareBtn.classList.add("share-button"); 
    shareBtn.setAttribute("title", "Share this section");
    
    // Indigo Share SVG
    shareBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81a3 3 0 0 0 3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9a3 3 0 0 0-3 3 3 3 0 0 0 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.15c-.05.21-.08.43-.08.66 0 1.61 1.31 2.91 2.92 2.91s2.92-1.3 2.92-2.91a2.92 2.92 0 0 0-2.92-2.91"/></svg>';

    shareBtn.onclick = (e) => {
      e.stopPropagation();
      e.preventDefault();
      
      // --- A. Extract Content ---
      
      // 1. Get Clean Title
      const tempClone = header.cloneNode(true);
      tempClone.querySelectorAll('.share-button, .headerlink').forEach(n => n.remove());
      const cleanTitle = tempClone.innerText.trim();

      // 2. Get Site Name & Author (Try Meta tags first, fallback to hardcoded)
      // MkDocs Material usually puts site name in og:site_name and author in meta[name="author"]
      const metaSiteName = document.querySelector('meta[property="og:site_name"]')?.content || "Okinawa is designed to fail";
      const metaAuthor = document.querySelector('meta[name="author"]')?.content || "りしき";

      // 3. Generate URL
      const shareUrl = window.location.origin + window.location.pathname + (header.id ? "#" + header.id : "");

      // --- B. Format Text for Viral Potential ---
      
      // Format: 
      // "Header Title"
      // via Site Name (by Author)
      const shareText = `"${cleanTitle}"\nvia ${metaSiteName} (by ${metaAuthor})`;
      
      // --- C. Execute Share ---

      if (navigator.share) {
        navigator.share({
          title: cleanTitle, // System dialog title
          text: shareText,   // The actual social media caption
          url: shareUrl      // The link
        }).catch(() => {});
      } else {
        // Fallback: Copy a pretty string to clipboard
        const clipboardText = `${shareText}\n${shareUrl}`;
        navigator.clipboard.writeText(clipboardText);
        
        // Optional: Replace alert with a temporary tooltip if you want it prettier, 
        // but alert is functional.
        alert("Link & Attribution copied to clipboard!");
      }
    };

    // 3. Move to the START (left side)
    header.prepend(shareBtn);
  });
});
