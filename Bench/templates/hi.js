let persons = [
    { id: 1, Name: 'Anne', status: true },
    { id: 2, Name: 'Beschi', status: false },
    { id: 3, Name: 'Cathrine', status: true },
    { id: 4, Name: 'Beschi', status: true }
];

let persons2 = [
    { id: 5, Name: 'Beschi', status: true },
    { id: 6, Name: 'James', status: false },
    { id: 7, Name: 'Beschi', status: true },
    { id: 8, Name: 'Leema', status: true }
];

let all = [...persons, ...persons2]
console.log(all.filter(item => item.Name === 'Beschi'))