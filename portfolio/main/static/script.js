// Mobile menu toggle
document.getElementById('mobile-menu-button').addEventListener('click', function() {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
            
            // Close mobile menu if open
            const mobileMenu = document.getElementById('mobile-menu');
            if (!mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('hidden');
            }
        }
    });
});

// Animation on scroll
const fadeElements = document.querySelectorAll('.fade-in');

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = 1;
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, {
    threshold: 0.1
});

fadeElements.forEach(element => {
    element.style.opacity = 0;
    element.style.transform = 'translateY(20px)';
    element.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
    observer.observe(element);
});

// Typing animation for hero section
const typingText = document.getElementById('typing-text');
if (typingText) {
  const messages = [
    'I love building web apps.',
    'I am a programmer.',
    'I am a coder.'
  ];
  let msgIdx = 0;
  let charIdx = 0;
  let isDeleting = false;

  function type() {
    const current = messages[msgIdx];
    if (!isDeleting) {
      typingText.textContent = current.slice(0, charIdx);
      charIdx++;
      if (charIdx > current.length) {
        isDeleting = true;
        setTimeout(type, 1200); // Pause before deleting
        return;
      }
    } else {
      typingText.textContent = current.slice(0, charIdx);
      charIdx--;
      if (charIdx < 0) {
        isDeleting = false;
        msgIdx = (msgIdx + 1) % messages.length;
        setTimeout(type, 400); // Pause before typing next
        return;
      }
    }
    setTimeout(type, isDeleting ? 40 : 80);
  }
  type();
}

// Optional: Add arrow navigation for horizontal slider (uncomment if desired)

const slider = document.getElementById('project-slider');

function scrollLeft() {
    slider.scrollBy({ left: -300, behavior: 'smooth' });
}

function scrollRight() {
    slider.scrollBy({ left: 300, behavior: 'smooth' });
}
// You can add buttons for previous/next and call these functions

