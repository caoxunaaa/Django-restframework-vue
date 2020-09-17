<template>
  <el-table
    :data="video_urls"
    style="width: 100%">
    <el-table-column
      label="上传日期"
      width="180" :formatter="formatDate">
      <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 10px">{{ scope.row.upload_time }}</span>
      </template>
    </el-table-column>

    <el-table-column
      label="文件名"
      width="180">
      <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.name }}</el-tag>
          </div>
        </el-popover>
      </template>
    </el-table-column>

    <el-table-column
      label="路径"
      width="180">
      <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.file_path }}</el-tag>
          </div>
        </el-popover>
      </template>
    </el-table-column>

    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleRun(scope.$index, scope.row)">播放
        </el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  name: 'VideosLayout',
  data () {
    return {
      video_urls: []
    }
  },
  mounted: function () {
    this.showVideo()
  },
  methods: {
    formatDate (row, column) {
      // 获取单元格数据
      let data = row[column.property]
      if (data == null) {
        return null
      }
      let dt = new Date(data)
      return dt.getFullYear() + '-' + (dt.getMonth() + 1) + '-' + dt.getDate() + ' ' + dt.getHours() + ':' + dt.getMinutes() + ':' + dt.getSeconds()
    },
    showVideo () {
      let that = this
      this.$axios({
        method: 'get',
        url: this.GLOBAL.BASE_URL + '/files/'
      }).then(function (response) {
        var res = response.data
        console.log(res)
        if (res) {
          that.video_urls = res
        } else {
          this.$message.error('查询视频失败')
          console.log(res['msg'])
        }
      })
    },
    handleRun (index, row) {
      console.log(this.video_urls[index].file_path)
      this.$router.push({path: '/video', query: {'file_path': this.video_urls[index].file_path}})
    },
    handleDelete (index, row) {
      console.log(index)
    }
  }

}
</script>

<style scoped>

</style>
