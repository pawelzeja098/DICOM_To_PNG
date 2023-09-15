var uploadedFileName = [];
let form = document.querySelector("form[id='upload-form']");



var myDropzone = new Dropzone("#kt_dropzonejs_example_1", {
    url: "../../../api/v1/kangaroo/file-upload",
    paramName: "file",
    maxFiles: 3,
    maxFilesize: 100, // MB
    addRemoveLinks: true,
    acceptedFiles : ".dcm",
    accept: function (file, done) {
        //if (file.name == "wow.jpg") {
        //    done("Naha, you don't.");
        //    uploadedFileName = file;
        done();
        uploadedFileName.push(file.name);
        

    }

});


myDropzone.on("complete", function (file) {
    // You can add your code to handle the response from the server here
    // For example, updating the UI with the server response
    if (file.status === "success") {
        const response = JSON.parse(file.xhr.response);
        const message = response.message;
        const el = document.getElementById("file_response");
        el.innerHTML =
            '<div class="alert alert-success alert-dismissible" role="alert">' +
            '   <div>' + message + '</div>' +
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
            '</div>';
    }
    else {
        const response = JSON.parse(file.xhr.response);
        const message = response.message;
        const el = document.getElementById("file_response");

        el.innerHTML =
            '<div class="alert alert-danger alert-dismissible" role="alert">' +
            '   <div>' + message + '</div>' +
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
            '</div>';

    }

});


function preview() {

    output.src = URL.createObjectURL(event.target.files[0]);
    output.hidden = false;

    

}

