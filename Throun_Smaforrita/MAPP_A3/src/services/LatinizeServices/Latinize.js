// A character map used to latinize strings
const characterMap = {
    '-' : ' ',
    '-' : '_',
    'a' : 'á|à|ã|â|ä|á',
    'A' : 'À|Á|Ã|Â|Ä|Á',
    'e' : 'é|è|ê|ë|é',
    'E':  'É|È|Ê|Ë|É',
    'i' : 'í|ì|î|ï|í',
    'I' : 'Í|Ì|Î|Ï|Í',
    'o' : 'ó|ò|ô|õ|ö|ó',
    'O' : 'Ó|Ò|Ô|Õ|Ö|Ó',
    'u' : 'ú|ù|û|ü|ú',
    'U' : 'Ú|Ù|Û|Ü|Ú',
    'c' : 'ç|Ç',
    'n' : 'ñ|Ñ',
    'd' : 'ð',
    'D' : 'Ð',
    'ae': 'æ',
    'Ae': 'Æ',
    'th': 'þ',
    'Th': 'Þ',
};

export function latinizeWord (TheName) {
    if (TheName) {
        // Replace spaces and special characters into a dash
        // var NewName = TheName.replace(/\s/g, '-')
        // Replace all non-latin characters with latin characters using the map above
        for (var mapPattern in characterMap) {
            TheName = TheName.replace(new RegExp(characterMap[mapPattern], 'g'), mapPattern);
        }
        // Remove all other non-latin characters if any remain
        //return NewName.replace(/[^A-Za-z0-9\s-]/g, '');
        return TheName
    }
    else{
        // Return false if the name was not a valid string
        return TheName;
    }
};
