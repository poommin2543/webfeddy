<template>
    <v-container fluid class="fill-height ma-0 pa-0">
        <v-navigation-drawer image="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg" permanent color="primary"
            width="250">
            <!-- <v-icon>home</v-icon> -->
            <v-card width="100%" height="10%" color="red" class="">
                <v-row no-gutters>
                    <v-card cols="2">
                        <v-sheet class="pl-5 mt-8">
                            <v-avatar color="blue">
                                <span class="text-h5">NP</span>
                            </v-avatar>
                        </v-sheet>
                    </v-card>
                    <v-card>
                        <v-sheet class="pl-5 mt-8 ">
                            <p>Admin</p>
                        </v-sheet>
                    </v-card>
                </v-row>
            </v-card>
            <v-card width="100%" height="30%" color="blue" class="">
                <v-card width="95%" height="95%" color="white" class="pa-0 ma-2 scrolling">
                    <v-list>
                        <v-list-item-group v-model="model" mandatory color="indigo">
                          <v-list-item
                            v-for="(item, i) in items"
                            :key="i"
                          >
                            <v-list-item-icon>
                              <v-icon v-text="item.icon"></v-icon>
                            </v-list-item-icon>
                  
                            <v-list-item-content>
                              <v-list-item-title v-text="item.text"></v-list-item-title>
                            </v-list-item-content>
                          </v-list-item>
                        </v-list-item-group>
                      </v-list>
                </v-card>
            </v-card>
            <v-card width="100%" height="30%" color="red" class="">

            </v-card>
        </v-navigation-drawer>
        <v-content class="fill-height">
            <v-card width="100%" height="25%" color="red" class="rounded-0">
                
            </v-card>
            <v-card width="100%" height="75%" color="blue" class="rounded-0">

            </v-card>
        </v-content>
    </v-container>
</template>
<script>
export default {
    data() {
        return {
            drawer: null,
            items: [
                {
                    icon: 'mdi-wifi',
                    text: 'Wifi',
                },
                {
                    icon: 'mdi-bluetooth',
                    text: 'Bluetooth',
                },
                {
                    icon: 'mdi-chart-donut',
                    text: 'Data Usage',
                },
                {
                    icon: 'mdi-chart-donut',
                    text: 'Data Usage',
                },
                {
                    icon: 'mdi-chart-donut',
                    text: 'Data Usage',
                },
                {
                    icon: 'mdi-chart-donut',
                    text: 'Data Usage',
                },
                {
                    icon: 'mdi-chart-donut',
                    text: 'Data Usage',
                },
            ],
        }

    },
}
</script>
<style>
.scrolling{
    overflow-y: auto;
}
</style>