module.exports = function(grunt) {

  grunt.initConfig({
    cssmin: {
      options: {
        shorthandCompacting: false,
        roundingPrecision: -1
      },
      target: {
        files: {
          'www/static_content/css/styles.min.css': ['www/static_content/css/reset.css','www/static_content/css/grid.css','www/static_content/css/general.css','www/static_content/css/header.css','www/static_content/css/nav.css','www/static_content/css/footer.css','www/static_content/css/alert_custom.css','www/static_content/css/buttons.css','www/static_content/css/forms.css','www/static_content/css/recipes_container_rectangles.css','www/static_content/css/other_options.css','www/static_content/css/status.css','www/static_content/css/comments.css','www/static_content/css/p_main_style.css','www/static_content/css/p_recipe.css']
        }
      }
    },
    uglify:{
      options:{
        banner:'/*Created by Nuno Machado*/\n'
      },
      build:{
        files:{
          "www/static_content/js/builds/engine.min.js":["www/static_content/js/alerts.js","www/static_content/js/popup_bar.js","www/static_content/js/main.js"],
          "www/static_content/js/builds/publish/publish.min.js":["www/static_content/js/publish/inputFileBtnFunctionality.js","www/static_content/js/publish/customClass.js"]
        }
      }
    },
    //tile images
    responsive_images: {
      dev: {
        options: {
          engine: 'im',
          sizes: [
            {
                name:'small',
                width: 236,
                quality:30
            },
            {
              name:'small_2x',
              width: 472,
              quality:30
            },
            {
              name:'medium',
              width: 322,
              quality:30
            },
            {
              name:'medium_2x',
              width: 644,
              quality:30
            },
            {
              name:'big',
              width: 380,
              quality:30
            },
            {
              name:'big_2x',
              width: 760,
              quality:30
            }
          ]
        },
        files: [{
          expand: true,
          src: ['*.{gif,jpg,png}'],
          cwd: 'image_or/tiles/',
          dest: 'www/static_content/assets/'
        }]
      }
    }
  });

  //build tasks
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  /*grunt.loadNpmTasks('grunt-responsive-images');*/
  grunt.registerTask('default', ['cssmin','uglify'/*,'responsive_images'*/]);
};
