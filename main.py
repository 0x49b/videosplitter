from tqdm import tqdm
import cv2
import os
import typer
import mimetypes

app = typer.Typer()


@app.command()
def split(source_path: str, output_path=os.path.join(os.getcwd(), 'frames')):
    if not os.path.exists(source_path):
        message = typer.style("The supplied argument is not an existing path to a file", fg=typer.colors.RED, bold=True)
        typer.echo(message)
        return

    elif not mimetypes.guess_type(source_path)[0].startswith('video'):
        message = typer.style("The supplied argument is not a video format", fg=typer.colors.RED, bold=True)
        typer.echo(message)
        return

    else:
        typer.echo("starting with video splitting")
        capture = cv2.VideoCapture(source_path)
        num_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

        for i in tqdm(range(num_frames), desc="Writing frames ", unit=' frames'):
            success, frame = capture.read()
            if success:
                framename = "frame_%s.jpg" % i
                path = os.path.join(output_path, framename)
                cv2.imwrite(path, frame)

        capture.release()
        typer.echo("finished splitting")


if __name__ == "__main__":
    app()
