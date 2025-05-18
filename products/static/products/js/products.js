document.addEventListener("DOMContentLoaded", function () {
    
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("delete-btn");
    const deleteConfirm = document.getElementById("deleteConfirm");
    
    
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
          let productId = e.currentTarget.getAttribute("data-product_id");
          deleteConfirm.href = `/products/delete/${productId}/`;
          deleteModal.show();
        });
      }
    }
);