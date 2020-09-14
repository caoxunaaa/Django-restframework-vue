<template>
  <div class="videos_layout">
    <el-row>
      <el-col :span="4"><div class="grid-content bg-purple">
        <router-link tag="a" target="_blank" :to="{path: '/video'}" class="routerWork">前往熊</router-link>
      </div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'VideosLayout'
}
</script>

<style scoped>

</style>
