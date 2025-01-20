
function showSpinner() {
    const spinnerContainer = document.getElementById('spinner-container');
    spinnerContainer.style.display = 'block';
}
function showPreview(event) {
    const file = event.target.files[0];
    const previewContainer = document.getElementById('preview-container');
    const previewImage = document.getElementById('preview-image');
    const previewPDF = document.getElementById('preview-pdf');
    if (file) {
        previewContainer.style.display = 'block';
        if (file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = function (e) {
                previewImage.src = e.target.result;
                previewImage.style.display = 'block';
                previewPDF.style.display = 'none';
            };
            reader.readAsDataURL(file);
        } else if (file.type === 'application/pdf') {
            previewImage.style.display = 'none';
            previewPDF.style.display = 'block';
            previewPDF.src = URL.createObjectURL(file);
        } else {
            previewContainer.style.display = 'none';
            alert('Unsupported file type. Please upload an image or PDF.');
        }
    }
}