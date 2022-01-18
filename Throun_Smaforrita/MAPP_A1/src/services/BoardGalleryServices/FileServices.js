import * as FileSystem from 'expo-file-system';

// ---------------------------------------------------------------------
// THESE FUNCTIONS ARE FROM THE PIXELMANIA PROJECT FROM THE LECTURES!
// ---------------------------------------------------------------------

const imageDirectory = `${FileSystem.documentDirectory}images`;

// Handling exceptions
const onException = (cb, errorHandler) => {
    try {
        return cb();
    } catch (err) {
        if (errorHandler) {
            return errorHandler(err);
        }
        console.error(err);
    }
}

// Cleaning out all images from the file system directory
export const cleanDirectory = async () => {
    await FileSystem.deleteAsync(imageDirectory);
}

// Copying a file from one location to another
export const copyFile = async (file, newLocation) => {
    return await onException(() => FileSystem.copyAsync({
        from: file,
        to: newLocation
    }));
}

// Adding an image to the gallery in BoardGalleryView
export const addImage = async imageLocation => {
    const folderSplit = imageLocation.split('/');
    const fileName = folderSplit[folderSplit.length - 1];
    await onException(() => copyFile(imageLocation, `${imageDirectory}/${fileName}`));

    return {
        name: fileName,
        type: 'image',
        file: await loadImage(fileName)
    };
}

// Removing an image from the gallery
export const remove = async name => {
    return await onException(() => FileSystem.deleteAsync(`${imageDirectory}/${name}`, { idempotent: true }));
}

// Loading up an image
export const loadImage = async fileName => {
    return await onException(() => FileSystem.readAsStringAsync(`${imageDirectory}/${fileName}`, {
        encoding: FileSystem.EncodingType.Base64
    }));
}

// Making sure there is a directory for storing the images in
const setupDirectory = async () => {
    const dir = await FileSystem.getInfoAsync(imageDirectory);
    if (!dir.exists) {
        await FileSystem.makeDirectoryAsync(imageDirectory);
    }
}

// For displaying all images in the gallery
export const getAllImages = async () => {
    // Check if directory exists
    cleanDirectory(`${FileSystem.documentDirectory}images/hi`)
    await setupDirectory();

    const result = await onException(() => FileSystem.readDirectoryAsync(imageDirectory));
    return Promise.all(result.map(async fileName => {
        return {
            name: fileName,
            type: 'image',
            file: await loadImage(fileName)
        };
    }));
}
