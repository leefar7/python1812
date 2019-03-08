  // <script>
  //   var swiper = new Swiper('.swiper-container', {
  //       pagination: '.swiper-pagination',
  //       nextButton: '.swiper-button-next',
  //       prevButton: '.swiper-button-prev',
  //       slidesPerView: 1,
  //       paginationClickable: true,
  //       spaceBetween: 30,
  //       autoplay: 2500,
  //       loop: true
  //   });
  //   </script>
 //
 $(function () {
      var topSwiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        autoplay: 3300,
        loop: true
    });
 })

  var mustbuySwiper = new Swiper('#mustbuySwiper', {
        paginationClickable: true,
        spaceBetween: 3,
        loop: true,
        autoplay: 3000,
        slidesPerView: 3,
        freeMode: true
    });