export type BilingualText = {
  en: string;
  zh: string;
};

export const profile = {
  name: 'GatsbyH',
  monogram: 'GATSBY',
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
      title: 'First Prize — 11th National College Student Statistical Modeling Competition, Zhejiang-Fujian Regional Selection',
      meta: 'Undergraduate Division · 2025',
      zh: '统计建模竞赛一等奖',
    },
    {
      title: 'Third Prize — 5th Yangtze River Delta University Mathematical Modeling Competition',
      meta: 'Undergraduate Division · 2025',
      zh: '长三角数学建模竞赛三等奖',
    },
    {
      title: 'Successful Participant — Mathematical Contest in Modeling (MCM)',
      meta: '2026',
      zh: '美国大学生数学建模竞赛',
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
