"""
cli integration for client microservice
"""

import click
import requests
import retry


@retry.retry
def badminton_backend_response(url, params, headers):


@click.command()
@click.option('--output_type', default="terminal",
              help='Output format for the current command, valid options are:' +
              'web, xlsx, terminal')
@click.option('--postal_code',
              help='Postal code used to filter options closest to centres')
@click.option('--map', default="True",
              help='Map generation for web interface')
@click.option('--path', default="True",
              help='Output path for excel files')
def badminton(output_type, postal_code, map):
    """Simple program that gets the badminton options for community centres in toronto area."""
    def get_params():
        params = {
            "output_type": output_type,
            "postal_code": postal_code,
            "map": map,
            "path:" path
        }
        return params

    def get_headers():
        headers = {
            "origin": "localhost",
        }
        return headers

    click.echo(f"Starting search!")

    activities_df = badminton_backend_response(
        local_url, params=get_params(), headers=get_headers())
    print(activities_df)


if __name__ == '__main__':
    badminton()
