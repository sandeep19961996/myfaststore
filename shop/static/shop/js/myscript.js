$('#slider2, #slider3, #slider4, #slider5, #slider6').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('#slider1').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 8,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('#slider7').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 8,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('#slider8').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 7,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function() {

    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amunt
            document.getElementById("totalamount").innerText = data.totalamunt
        }
    })

})

$('.minus-cart').click(function() {

    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amunt
            document.getElementById("totalamount").innerText = data.totalamunt
        }
    })

})
$('.remove-cart').click(function() {
        var id = $(this).attr("pid").toString();
        var eml = this
        $.ajax({
            type: "GET",
            url: "/removecart",
            data: {
                prod_id: id
            },
            success: function(data) {
                document.getElementById("amount").innerText = data.amunt
                document.getElementById("totalamount").innerText = data.totalamunt
                eml.parentNode.parentNode.parentNode.parentNode.remove()
            }
        })
    })
    // var loader = document.getElementById("preloader")
    // window.addEventListener("load", function() {
    //     loader.style.display = 'none'
    // })

// $(document).ready(function(){
// 	$('div#loading').removeAttr('id');
// });
var preloader = document.getElementById("loading");
// window.addEventListener('load', function(){
// 	preloader.style.display = 'none';
// 	})

function myFunction() {
    preloader.style.display = 'none';
};

$('document').ready(function(e) {

    $(".loader").fadeOut("slow");

});