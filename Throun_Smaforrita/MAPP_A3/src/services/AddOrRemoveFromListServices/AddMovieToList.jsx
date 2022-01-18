
// A function for adding a movie to a movie list if it is not already within the list
export const addToMovieList = (MovieList, NewMovie) => {
    var inList = false;
    if (!MovieList.includes(NewMovie)){
        MovieList.map((movie) => {
            if (movie.title === NewMovie.title) {
                inList = true;
            }
        })
        if (!inList) {
            MovieList.push(NewMovie);
        }
    }
    return MovieList;
};
