const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();
const port = 3000;

// Configure multer for file storage
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/')
    },
    filename: function (req, file, cb) {
        // Use Date.now() to make each filename unique
        cb(null, Date.now() + path.extname(file.originalname))
    }
});

const upload = multer({ storage: storage });

// Serve static files from public directory
app.use(express.static('public'));

// Handle file upload
app.post('/upload', upload.single('file'), (req, res) => {
    if (req.file) {
        console.log('File uploaded successfully:', req.file.path);
        res.send({ message: 'File uploaded successfully', filePath: req.file.path });
    } else {
        res.status(400).send({ message: 'Please upload a file' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
