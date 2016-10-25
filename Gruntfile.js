module.exports = function(grunt) {

  grunt.initConfig({
    cssmin: {
      options: {
        shorthandCompacting: false,
        roundingPrecision: -1
      },
      target: {
        files: {
          'www/static_content/css/styles.min.css': ['www/static_content/css/reset.css','www/static_content/css/grid.css','www/static_content/css/general.css','www/static_content/css/header.css','www/static_content/css/nav.css','www/static_content/css/footer.css']
        }
      }
    },
    uglify:{
      options:{
        banner:'/*Created by Nuno Machado*/\n'
      },
      build:{
        files:{

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
