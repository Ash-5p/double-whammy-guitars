/* jshint esversion: 11, jquery: true */

document.addEventListener("DOMContentLoaded", function () {
    
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("delete-btn");
    const deleteConfirm = document.getElementById("deleteConfirm");
    
    
    /**
     * Delete faq event listener
     */
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
          let faqId = e.currentTarget.getAttribute("data-faq_id");
          deleteConfirm.href = `/faqs/delete/${faqId}/`;
          deleteModal.show();
        });
      }

    $('.btt-link').click(function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
        
    $('.gtb-link').click(function(e) {
            e.preventDefault();
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        });
    }
);