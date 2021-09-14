<template>
  <div class="container-fluid">
    <div class="d-flex bd-highlight">
      <div class="p-2 w-25 flex-shrink-1 bd-highlight">
        <draggable class="dragArea list-group" :list="list1" :group="{ name: 'people', pull: 'clone', put: false }"
                   @change="log">
          <div class="list-group-item" v-for="element in list1" :key="element.name">
            {{ element.name }}
          </div>
        </draggable>
      </div>

      <div class="p-2 w-75 bd-highlight">
        <draggable class="dragArea list-group" :list="list2" group="people" @change="log">
          <div class="list-group-item" v-for="element in list2" :key="element.name">
            <!--            {{ element.name }}-->
            <div class="card">
              <div class="card-header">
                {{ element.name }}
                <div class="btn-group float-end" role="group" aria-label="Basic example">
                  <button type="button" class="btn btn-primary">Left</button>
                  <button type="button" class="btn btn-primary">Middle</button>
                  <button type="button" class="btn btn-primary">Right</button>
                </div>
              </div>
              <div class="card-body">
                <template v-if="element.question_type === 'single'">
                  <input :type="element.type">
                </template>

                <template v-else>
                  <ol>
                    <li v-for="(option,index) in element.options">
                      <input :type="element.type"><input v-model="option.title" placeholder="Title" type="text">
                      <button @click="element.options.splice(index,1)">x</button>
                    </li>
                  </ol>
                  <button @click="element.options.push({title : ''})">+</button>
                </template>
              </div>
            </div>
          </div>
        </draggable>
      </div>
    </div>
  </div>
</template>

<script>
import draggable from 'vuedraggable'

export default {
  name: 'Helloworld',
  components: {
    draggable
  },
  data() {
    return {
      list1: [
        {name: "John", id: 1},
        {name: "Joao", id: 2},
        {name: "Jean", id: 3},
        {name: "Gerard", id: 4}
      ],
      list2: [
        {id: 5, name: 'Hello 5', question_type: 'single', type: 'text', options: []},
        {id: 4, name: 'Hello 9', question_type: 'single', type: 'file', options: []},
        {id: 6, name: 'Hello 3', question_type: 'multiple', type: 'date', options: []},
        {id: 1, name: 'Hello 8', question_type: 'single', type: 'time', options: []},
        {id: 9, name: 'Hello 6', question_type: 'multiple', type: 'radio', options: []},
      ]
    }
  },
  methods: {
    log() {

    }
  }
};
</script>
