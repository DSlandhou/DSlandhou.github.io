export type BilingualText = {
  en: string;
  zh: string;
};

export const profile = {
  name: 'GatsbyH',
  monogram: 'BC.',
  handle: 'DSlandhou',
  location: 'Hangzhou, China',
  email: 'bernardinocristian718@gmail.com',
  github: 'https://github.com/DSlandhou',
  instagram: '',
  x: '',
  introduction: {
    en: 'Information Management and Information Systems at Zhejiang University.',
    zh: '浙江大学信息管理与信息系统',
  },
  currentFocus: [
    
    { en: 'Build a disciplined study system', zh: '建立稳定的学习系统' },
    { en: 'Find an internship opportunity', zh: '寻找实习机会' },
    { en: 'Prepare graduate applications abroad', zh: '准备海外研究生申请' },
  ] satisfies BilingualText[],
  education: [
    {
      time: '2022 — Present',
      title: 'Zhejiang University',
      detail: 'B.S. in Information Management and Information Systems',
      zh: '浙江大学 · 信息管理与信息系统本科',
    },
  ],
  publications: [
    {
      title: 'Publication slot — add your first paper here',
      meta: 'Authors · Journal or Conference · Year',
      zh: '论文发表预留位',
    },
  ],
  awards: [
    {
      title: 'Academic award slot — add an achievement here',
      meta: 'Awarding organisation · Year',
      zh: '学术奖项预留位',
    },
  ],
  skills: [
    {
      area: { en: 'Research', zh: '研究' },
      items: ['Literature review', 'Academic writing', 'Information analysis'],
    },
    {
      area: { en: 'Data', zh: '数据' },
      items: ['SQL', 'Python', 'Data visualisation'],
    },
    {
      area: { en: 'Product & Web', zh: '产品与网页' },
      items: ['Information architecture', 'Astro', 'GitHub'],
    },
  ],
};
