function wrapper() {
 
    var reveals = document.querySelectorAll(".wrapper");
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
     
      if (elementTop < 0) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  
  }
  window.addEventListener("scroll", wrapper);