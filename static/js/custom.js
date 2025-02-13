
// Initialize Swiper
const swiper = new Swiper('.swipermain', {
    loop: true, // Enable continuous looping
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    autoplay: {
        delay: 3000, // Auto-slide delay in milliseconds
        disableOnInteraction: false, // Continue autoplay after user interaction
    },
    spaceBetween: 30, // Space between slides
    slidesPerView: 1, // Show 1 slide at a time
});

// LOGIN JS


document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form submission for demo
  
    const submitButton = document.querySelector('.btn-submit');
    submitButton.classList.add('loading'); // Add loading class
  
    // Simulate form submission delay
    setTimeout(() => {
      submitButton.classList.remove('loading'); // Remove loading class
      alert('Form submitted successfully!'); // Show success message
    }, 2000); // 2-second delay
  });