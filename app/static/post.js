$(document).ready(function () {
  $('.attach').on('change', function () {
    var input = this;
    var form = $(input).closest('form');
    var file = input.files[0];
    var reader = new FileReader();

    reader.onloadend = function () {
      form.find('.image-preview').remove();

      if (reader.result) {
        var newImage = $('<img>', { class: 'image-preview', src: reader.result, alt: 'Image Preview' });
        form.find('.image-preview-container').append(newImage);
      }
    };

    if (file) {
      reader.readAsDataURL(file);
    }
  });
});