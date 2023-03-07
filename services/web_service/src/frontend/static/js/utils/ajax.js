export function upload(data, url, callback) {
    const formData = new FormData();
    formData.append('file', data);

    fetch(url, {
      method: 'POST',
      body: formData
    })
    .then((response) => response.json())
    .then(callback)
    .catch((error) => {
      console.error('Error:', error);
    });
}