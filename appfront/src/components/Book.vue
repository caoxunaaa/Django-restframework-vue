<template>
  <div class="home">
    <Header></Header>
    <el-row display="margin-top:10px">
      <el-input v-model="add" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="addBook()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row display="margin-top:10px">
      <el-input v-model="remove" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="warning" @click="removeBook()" style="float:left; margin: 2px;">删除</el-button>
    </el-row>
    <el-row>
      <el-table :data="bookList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
        </el-table-column>
        <el-table-column prop="book_name" label="书名" min-width="100">
        </el-table-column>
        <el-table-column prop="create_time" label="添加时间" min-width="100">
        </el-table-column>
      </el-table>
    </el-row>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './header'
import Footer from './footer'

export default {
  name: 'Book',
  components: {
    Header,
    Footer
  },
  data () {
    return {
      add: '',
      remove: '',
      bookList: []
    }
  },
  mounted: function () {
    this.showBooks()
  },
  methods: {
    addBook () {
      let that = this
      this.$axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/books/',
        data: {
          book_name: that.add
        }
      }).then(function (response) {
        var res = response.data
        console.log(res)
        if (res) {
          that.showBooks()
        } else {
          this.$message.error('新增书籍失败，请重试')
          console.log(res['msg'])
        }
      })
    },
    removeBook () {
      let that = this
      this.$axios({
        method: 'delete',
        url: 'http://127.0.0.1:8000/books/' + that.remove
      }).then(function (response) {
        console.log(response)
        var res = response.data
        console.log(res)
        that.showBooks()
      })
    },
    showBooks () {
      let that = this
      this.$axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/books/'
      }).then(function (response) {
        var res = response.data
        console.log(res)
        if (res) { that.bookList = res } else {
          this.$message.error('查询书籍失败')
          console.log(res['msg'])
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
