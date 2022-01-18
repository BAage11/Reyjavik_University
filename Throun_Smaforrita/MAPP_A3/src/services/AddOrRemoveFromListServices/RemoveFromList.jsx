// A function for removing a movie from a movie list
export const removeMovieFromList = (MovieList, OldMovie) => {
    MovieList.map((movie, index, arr) => {
        if ( OldMovie.title === movie.title) {
            arr.splice(index, 1);
        }
    });
    return MovieList;
};
