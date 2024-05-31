import { defineStore } from "pinia";

/**
 * 网站数据
 */
const useSiteDataStore = defineStore("siteData", {
  state: () => {
    return {
      siteTitle: import.meta.env.VITE_SITE_TITLE,
      songPicColor: "rgb(128,128,128)",
      searchInputActive: false,
    };
  },
  getters: {},
  actions: {},
  persist: [
    {
      storage: localStorage,
      paths: [""],
    },
  ],
});

export default useSiteDataStore;
