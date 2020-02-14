
// function groupIdx(sheet, findGroup) {
//     for (let i in sheet.groups) {
//         let group = sheet.groups[i];
//         if (group.name.includes(findGroup) || group.nameFr.includes(findGroup))
//             return i;
//     }
//     return -1;
// }

// function findGroupKey(groups, substr) {
//     for (let g of groups)
//         if (g.includes(substr))
//             return g;
//     return '';
// }

function filterGroup(volume, filterGroup) {
    for (let sheet of Object.values(volume)) {
        if (sheet.data.hasOwnProperty(filterGroup)) // filtering row
            delete sheet.data[filterGroup];
        else {   // filtering column
            for (let data of Object.values(sheet.data))
                if (data.hasOwnProperty(filterGroup))
                    delete data[filterGroup];
            for (let i in sheet.groups)
                if (sheet.groups[i] == filterGroup)
                    sheet.groups.splice(i, 1);
        }
    }
}

function transpose(data) {
    let res = {};
    for (let row of Object.keys(data)) {
        for (let col of Object.keys(data[row])) {
            if (!res.hasOwnProperty(col))
                res[col] = {};
            res[col][row] = data[row][col];
        }
    }
    return res;
}


function loadDataFull(urlBase) {

    const url = urlBase + 'data/parsed/all.json';
    let data = {};
    $.getJSON(url, (obj) => {
        data = obj;
    });
    console.log(data);
    return data;
}

function volumeIndex(url) {
    return fetch(url + 'index.txt')
        .then((response) => {
            return response.text();
        })
        .then((text) => {
            return text.split('\n');
        });
}

function volumeNames(url) {
    return volumeIndex(url).then((Index) => {
        return Index.map((str) => /([^\/\n]+)\.json/g.exec(str)[1])
    });
}

function loadData(urlData) {

    // const urlData = urlBase + 'data/parsed/';
    const urlIndex = urlData + 'index.txt';

    return volumeIndex(urlIndex).then((volIndex) => {
        let urlIndex = volIndex.map((relUrl) => { return urlData + relUrl; });
        for (i in volIndex)
            $.getJSON(urlData + volIndex[i], (obj) => {
                data.push(obj);
            });

        // var data = [];
        // for (url of Object.values(Index))
        //     $.getJSON(url, (obj) => {
        //         data.push(obj);
        //     });
        return data;
    });
}
