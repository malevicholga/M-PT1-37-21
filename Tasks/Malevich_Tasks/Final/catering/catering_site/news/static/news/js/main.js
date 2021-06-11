window.addEventListener("DOMContentLoaded", () => {
  // sidebar
  const iconMenu = document.querySelector(".menu__icon");
  const menuBody = document.querySelector(".menu__body");
  const menuLinks = document.querySelectorAll(".menu__link");

  if (iconMenu) {
    iconMenu.addEventListener("click", () => {
      document.body.classList.toggle("_lock");
      iconMenu.classList.toggle("_active");
      menuBody.classList.toggle("_active");
    });
  }

  menuLinks.forEach((item) => {
    item.addEventListener("click", () => {
      if (iconMenu.classList.contains("_active")) {
        document.body.classList.remove("_lock");
        iconMenu.classList.remove("_active");
        menuBody.classList.remove("_active");
      }
    });
  });
  if (iconMenu.classList.contains("_active")) {
    document.body.classList.remove("_lock");
    iconMenu.classList.remove("_active");
    menuBody.classList.remove("_active");
  }

  //===== прокрутка
  const smoothLinks = document.querySelectorAll('a[href^="#"]');
  for (let smoothLink of smoothLinks) {
    smoothLink.addEventListener("click", function (e) {
      e.preventDefault();

      const id = smoothLink.getAttribute("href");
      document.querySelector(id).scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    });
  }

  //slider
  const swiper = new Swiper(".swiper-container", {
    speed: 1500,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    autoplay: {
      delay: 2500,
    },
  });

  menuLinks.forEach((item) => {
    item.addEventListener("click", (e) => {
      menuLinks.forEach((elem) => {
        if (elem === item) {
          item.classList.add("active");
        } else {
          elem.classList.remove("active");
        }
      });
    });
  });
});
