export type AlbumCover = {
  title: string;
  year: string;
  artwork?: string;
  treatment?: 'disc';
};

// Latest note #1 uses the first sleeve, latest note #2 uses the second, and so on.
// Artwork is shown in grayscale so it fits the site's black, white, and soft-gray system.
export const kanyeAlbumRotation: AlbumCover[] = [
  {
    title: 'The College Dropout',
    year: '2004',
    artwork: 'https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/15/05/09/15050911-a2f1-9ebc-0d16-6e8faad1cf80/00602567924326.rgb.jpg/600x600bb.jpg',
  },
  {
    title: 'Late Registration',
    year: '2005',
    artwork: 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/0e/90/3c/0e903c43-9d81-f91b-90f1-727a58f7fb2c/00602498824030.rgb.jpg/600x600bb.jpg',
  },
  {
    title: 'Graduation',
    year: '2007',
    artwork: 'https://is1-ssl.mzstatic.com/image/thumb/Music128/v4/39/25/2d/39252d65-2d50-b991-0962-f7a98a761271/00602517483507.rgb.jpg/600x600bb.jpg',
  },
  {
    title: '808s & Heartbreak',
    year: '2008',
    artwork: 'https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/f3/61/19/f36119b9-4d88-05eb-4306-2ae0e7decf88/08UMGIM26559.rgb.jpg/600x600bb.jpg',
  },
  {
    title: 'My Beautiful Dark Twisted Fantasy',
    year: '2010',
    artwork: 'https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/d1/74/da/d174dacf-5782-dfe2-19f7-ce037dcd0237/00602527584935.rgb.jpg/600x600bb.jpg',
  },
  { title: 'Yeezus', year: '2013', treatment: 'disc' },
  {
    title: 'The Life of Pablo',
    year: '2016',
    artwork: 'https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/ec/fd/e0/ecfde04e-6db2-e55e-41fe-83c87a52b16e/00602547908339.rgb.jpg/600x600bb.jpg',
  },
  {
    title: 'ye',
    year: '2018',
    artwork: 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/f8/92/62/f892628e-bfd5-2437-c1f5-0ebbd366de09/00602577303098.rgb.jpg/600x600bb.jpg',
  },
  {
    title: 'KIDS SEE GHOSTS',
    year: '2018',
    artwork: 'https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/3f/2e/d3/3f2ed3b1-d260-4e92-816b-4beac102c676/00602567794318.rgb.jpg/600x600bb.jpg',
  },
  {
    title: 'Watch the Throne',
    year: '2011',
    artwork: 'https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/18/f5/07/18f5070d-b5dc-796c-bce4-42badb41a762/00602527812526.rgb.jpg/600x600bb.jpg',
  },
];
