/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
     $('.scrollspy').scrollSpy();
    // $('.slider').slider();
    // $(".collapsible").collapsible();
    // $("#copyright").text(new Date().getFullYear());
    // $("select").formSelect();
    // $(".datepicker").datepicker({
    //     format: "dd mmmm, yyyy",
    //     yearRange: 3,
    //     showClearBtn: true,
    //     i18n: {
    //         done: "Select"
    //     }
    });

//   validateMaterializeSelect();
//     function validateMaterializeSelect() {
//         let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
//         let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
//         if ($("select.validate").prop("required")) {
//             $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
//         }
//         $(".select-wrapper input.select-dropdown").on("focusin", function () {
//             $(this).parent(".select-wrapper").on("change", function () {
//                 if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
//                     $(this).children("input").css(classValid);
//                 }
//             });
//         }).on("click", function () {
//             if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
//                 $(this).parent(".select-wrapper").children("input").css(classValid);
//             } else {
//                 $(".select-wrapper input.select-dropdown").on("focusout", function () {
//                     if ($(this).parent(".select-wrapper").children("select").prop("required")) {
//                         if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
//                             $(this).parent(".select-wrapper").children("input").css(classInvalid);
//                         }
//                     }
//                 });
//             }
//         });
//     }  
// });



// // add new cloned 'direction'
//     $(".add-direction").on("click", function () {
//         addDirection($(this).parent(".new-direction"));
//     });
//     function addDirection(thisObj) {
//         // clone and remove existing values
//         $(".new-direction:first").clone(true, true).insertAfter(thisObj).find("textarea").val("");
//         directionCount += 1;
//         // custom Materialize validation (not built-in natively)
//         thisObj.closest("div").find("textarea").focus();
//         disableRemoveDirection();
//         validateMaterializeSelect();
//         thisObj.next("div").find("textarea").focus();
//         // end custom validation
//     }


    // // delete selected 'direction'
    // $(".remove-direction").on("click", function () {
    //     removeDirection($(this).parent(".new-direction"));
    // });
    // function removeDirection(thisObj) {
    //     $(thisObj).remove();
    //     directionCount -= 1;
    //     disableRemoveDirection();
    // }
    // // disable 'remove-direction' if only one direction exists
    // let directionCount = $(".direction").length;
    // disableRemoveDirection();
    // function disableRemoveDirection() {
    //     if (directionCount === 1) {
    //         $("button.remove-direction").prop("disabled", true);
    //     } else {
    //         $("button.remove-direction").prop("disabled", false);
    //     }
    // }